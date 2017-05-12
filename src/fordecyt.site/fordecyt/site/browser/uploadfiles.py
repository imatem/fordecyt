# -*- coding: utf-8 -*-

from plone import api
from z3c.form import button
from z3c.form import form

import logging
import os

from plone.i18n.normalizer import idnormalizer as idn
from plone.namedfile.file import NamedBlobFile
from plone.namedfile.file import NamedBlobImage

logger = logging.getLogger('Plone')


class UploadFoldersForm(form.Form):
    """Upload information of fordecyt."""

    @button.buttonAndHandler(u'Upload folders structure')
    def handle_upgrade_folders(self, action):
        """Copy structure folders by fordecyt."""
        logger.info('Here we go ...')

        client_path = os.path.abspath(os.curdir)
        directory_path = client_path + '/Extensions/'
        portal = api.portal.get()
        container_folder = portal
        print container_folder
        for root, dirs, files in os.walk(directory_path):

            for directory in dirs:
                newlist = [idn.normalize(item) for item in root.split('/')[6:]]
                new_path_container = '/'.join(filter(None, newlist))
                newcontainer = portal.unrestrictedTraverse(new_path_container)
                api.content.create(type='Folder', id=idn.normalize(directory), title=directory, container=newcontainer)

            for file in files:
                path_list = [idn.normalize(item) for item in root.split('/')[6:]]
                new_path_container_file = '/'.join(filter(None, path_list))
                newcontainer = portal.unrestrictedTraverse(new_path_container_file)
                # pdf files
                if file.lower().endswith(".pdf"):
                    uploadfile = api.content.create(
                        type='File',
                        id=idn.normalize(file),
                        title=file,
                        container=newcontainer)
                    filename = os.path.join(root, file)
                    try:
                        fileRawData = open(filename)
                    except Exception:
                        print 'File not found: {}'.format(filename)
                        continue

                    uploadfile.file = NamedBlobFile(
                        data=fileRawData.read(),
                        contentType='application/pdf',
                        filename=unicode(file, 'utf-8'))

                    uploadfile.reindexObject()
                    fileRawData.close()
                # images
                if file.lower().endswith(('.jpg', '.jpeg', '.gif', '.png')):
                    uploadfile = api.content.create(
                        type='Image',
                        id=idn.normalize(file),
                        title=file,
                        container=newcontainer)
                    filename = os.path.join(root, file)
                    uploadfile.image = NamedBlobImage(
                        data=open(filename, 'r').read(),
                        filename=unicode(file, 'utf-8'))
                    uploadfile.reindexObject()

        logger.info('done.')


# def upload_files(self):
#     year = '2016'
#     path = '/acerca-de/estructura-interna/secretaria-academica/informes/investigadores'
#     uploadfolder = api.content.get(path='/'.join((path, year, 'pdf')))
#     reports = api.content.find(
#         context=api.content.get(path='/'.join((path, year))),
#         portal_type='CVFolder')
#     instancepath = os.path.abspath(os.curdir)
#     for report in reports:
#         pdf = '{0}-anual-{1}.pdf'.format(report.id, year)
#         FILE = os.path.join(instancepath, 'Extensions/informes', pdf)
#         try:
#             fileRawData = open(FILE)
#         except Exception:
#             print 'File not found: {}'.format(FILE)
#             continue
#         uploadfolder.invokeFactory('File', id=report.id, title=report.id)
#         uploadfolder[report.id].setFile(fileRawData)
#         uploadfolder[report.id].setTitle(report.id)
#         uploadfolder[report.id].reindexObject()
#         fileRawData.close()
#     print 'Done'
