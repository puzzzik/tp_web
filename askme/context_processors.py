from askme.models import Tag, Profile

def add_variable_to_context(request):
    return {
        'hot_tags': Tag.manager.get_hot_tags(),
        'hot_users': Profile.manager.get_hot_users()
    }