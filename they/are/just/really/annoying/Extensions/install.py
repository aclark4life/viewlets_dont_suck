from Products.CMFCore.utils import getToolByName

def uninstall(portal):
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-they.are.just.really.annoying:uninstall')
    return "Uninstalled viewlets don't suck!"

