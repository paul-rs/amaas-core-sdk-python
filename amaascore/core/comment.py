from __future__ import absolute_import, division, print_function, unicode_literals

from amaascore.core.amaas_model import AMaaSModel


class Comment(AMaaSModel):

    def __init__(self, comment_value, active=True, *args, **kwargs):
        self.comment_value = comment_value
        self.active = active
        super(Comment, self).__init__(*args, **kwargs)
