# -*- coding: utf-8 -*-
class MilmoveRouter(object):
    """
    DB router to direct milmove models to their own database.
    See https://docs.djangoproject.com/en/3.0/topics/db/multi-db/
    """

    milmove_app_labels = ["milmove_app", "milmove_custom"]

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.milmove_app_labels:
            return "milmove"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.milmove_app_labels:
            return "milmove"
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.milmove_app_labels
            and obj2._meta.app_label in self.milmove_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.milmove_app_labels:
            return False
        return None
