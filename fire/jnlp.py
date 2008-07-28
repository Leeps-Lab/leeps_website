import xml.dom.minidom

def fixed_writexml(self, writer, indent="", addindent="", newl=""):
    writer.write(indent+"<" + self.tagName)

    attrs = self._get_attributes()
    a_names = attrs.keys()
    a_names.sort()

    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        xml.dom.minidom._write_data(writer, attrs[a_name].value)
        writer.write("\"")
    if self.childNodes:
        if len(self.childNodes) == 1 \
          and self.childNodes[0].nodeType == xml.dom.minidom.Node.TEXT_NODE:
            writer.write(">")
            self.childNodes[0].writexml(writer, "", "", "")
            writer.write("</%s>%s" % (self.tagName, newl))
            return
        writer.write(">%s"%(newl))
        for node in self.childNodes:
            node.writexml(writer,indent+addindent,addindent,newl)
        writer.write("%s</%s>%s" % (indent,self.tagName,newl))
    else:
        writer.write("/>%s"%(newl))
# replace minidom's function with ours
xml.dom.minidom.Element.writexml = fixed_writexml

def new_argument(doc, arg):
    argument = doc.createElement("argument")
    argument.appendChild(doc.createTextNode(arg))
    return argument

def create_jnlp(username, password, server, kindling, configuration):
    doc = xml.dom.minidom.Document()
    jnlp = doc.createElement("jnlp")
    jnlp.setAttribute("spec", "1.0+")
    jnlp.setAttribute("codebase",
            "http://econlab.ucsc.edu/experiments/")
    doc.appendChild(jnlp)

    information = doc.createElement("information")
    title = doc.createElement("title")
    title.appendChild(doc.createTextNode("FIRE"))
    vendor = doc.createElement("vendor")
    vendor.appendChild(doc.createTextNode("LEEPS"))
    homepage = doc.createElement("homepage")
    homepage.setAttribute("href", "http://econlab.ucsc.edu/")
    information.appendChild(title)
    information.appendChild(vendor)
    information.appendChild(homepage)
    jnlp.appendChild(information)

    security = doc.createElement("security")
    security.appendChild(doc.createElement("all-permissions"))
    jnlp.appendChild(security)

    resources = doc.createElement("resources")

    j2se = doc.createElement("j2se")
    j2se.setAttribute("version", "1.4+")
    resources.appendChild(j2se)

    jar = doc.createElement("jar")
    jar.setAttribute("href", "FIRE-Spark.jar")
    resources.appendChild(jar)

    jar = doc.createElement("jar")
    jar.setAttribute("href", "FIRE-Libraries.jar")
    resources.appendChild(jar)

    jnlp.appendChild(resources)

    application_desc = doc.createElement("application-desc")
    application_desc.setAttribute(
            "main-class",
            "edu.ucsc.leeps.fire.spark.SparkApp")

    application_desc.appendChild(new_argument(doc, "-u"))
    application_desc.appendChild(new_argument(doc, username))
    application_desc.appendChild(new_argument(doc, "-p"))
    application_desc.appendChild(new_argument(doc, password))
    application_desc.appendChild(new_argument(doc, "-s"))
    application_desc.appendChild(new_argument(doc, server))
    application_desc.appendChild(new_argument(doc, "-k"))
    application_desc.appendChild(new_argument(doc, kindling))
    application_desc.appendChild(new_argument(doc, "-c"))
    application_desc.appendChild(new_argument(doc, configuration))

    jnlp.appendChild(application_desc)

    return doc.toprettyxml()

if __name__ == "__main__":
    print create_jnlp(
            "admin", "macinam071", "econlab.ucsc.edu",
            "http://econlab.ucsc.edu/site_media/fire/kindling/kindling.jar",
            "http://econlab.ucsc.edu/site_media/fire/configuration/config.xml")
