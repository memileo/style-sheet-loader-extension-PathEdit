from .style_sheet_loader import StyleSheetLoader

# And add the extension to Krita's list of extensions:
app = Krita.instance()
# Instantiate your class:
extension = StyleSheetLoader(parent = app)
app.addExtension(extension)
