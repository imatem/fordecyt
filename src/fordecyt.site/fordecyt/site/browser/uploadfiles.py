# -*- coding: utf-8 -*-

from DateTime import DateTime
# from openpyxl import load_workbook
from plone import api
from z3c.form import button
from z3c.form import form

import logging
import os

from plone.i18n.normalizer import idnormalizer as idn

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
        container_folder = portal.unrestrictedTraverse('documents/')
        print container_folder
        for root, dirs, files in os.walk(directory_path):

            for directory in dirs:
                newlist = [idn.normalize(item) for item in root.split('/')[6:]]
                new_path_container = 'documents/' + '/'.join(filter(None, newlist))
                newcontainer = portal.unrestrictedTraverse(new_path_container)
                api.content.create(type='Folder', title=directory, container=newcontainer)

            # for file in files:
            #     if file.endswith(".pdf"):
            #         print(os.path.join(root, file))

        logger.info('done.')
