import ckan.plugins as plugins
import ckan.plugins.toolkit as tk
from ckan.plugins.toolkit import Invalid

def is_anzlic(value):
    if value is None or not value:
        return
    if not value.startswith('ANZVI080') and not value.startswith('anzvi080'):
        raise Invalid('This is not in the Victorian ANZLIC format')
    if not len(value) == 15:
        raise Invalid('Anzlic IDs must be 15 characters in length, this id has  '+str(len(value)))
    return value.upper()


class DelwpdataPlugin(plugins.SingletonPlugin,tk.DefaultDatasetForm):
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def is_fallback(self):
        return True

    def package_types(self):
        return []

    def update_config(self, config_):
        tk.add_template_directory(config_, 'templates')
        tk.add_public_directory(config_, 'public')
        tk.add_resource('fanstatic', 'delwpdata')

    def _modify_package_schema(self, schema):
        schema.update({
            'anzlic_id': [tk.get_validator('ignore_missing'),is_anzlic,tk.get_converter('convert_to_extras')]
        })
        return schema

    def create_package_schema(self):
        schema = super(DelwpdataPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(DelwpdataPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(DelwpdataPlugin, self).show_package_schema()
        schema.update({
            'anzlic_id': [tk.get_converter('convert_from_extras'),tk.get_validator('ignore_missing')]
        })
        return schema

