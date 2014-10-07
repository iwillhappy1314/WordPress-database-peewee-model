from peewee import *

database = MySQLDatabase('www', **{'user': "'root'"})

class UnknownField(object):
    pass

class BaseModel(Model):
    class Meta:
        database = database

class WpCommentmeta(BaseModel):
    comment = BigIntegerField(db_column='comment_id')
    meta = BigIntegerField(db_column='meta_id', primary_key=True)
    meta_key = CharField(max_length=255, null=True)
    meta_value = TextField(null=True)

    class Meta:
        db_table = 'wp_commentmeta'

class WpComments(BaseModel):
    comment = BigIntegerField(db_column='comment_ID', primary_key=True)
    comment_agent = CharField(max_length=255)
    comment_approved = CharField(max_length=20)
    comment_author = TextField()
    comment_author_ip = CharField(db_column='comment_author_IP', max_length=100)
    comment_author_email = CharField(max_length=100)
    comment_author_url = CharField(max_length=200)
    comment_content = TextField()
    comment_date = DateTimeField()
    comment_date_gmt = DateTimeField()
    comment_karma = IntegerField()
    comment_parent = BigIntegerField()
    comment_post = BigIntegerField(db_column='comment_post_ID')
    comment_type = CharField(max_length=20)
    user = BigIntegerField(db_column='user_id')

    class Meta:
        db_table = 'wp_comments'

class WpLinks(BaseModel):
    link_description = CharField(max_length=255)
    link = BigIntegerField(db_column='link_id', primary_key=True)
    link_image = CharField(max_length=255)
    link_name = CharField(max_length=255)
    link_notes = TextField()
    link_owner = BigIntegerField()
    link_rating = IntegerField()
    link_rel = CharField(max_length=255)
    link_rss = CharField(max_length=255)
    link_target = CharField(max_length=25)
    link_updated = DateTimeField()
    link_url = CharField(max_length=255)
    link_visible = CharField(max_length=20)

    class Meta:
        db_table = 'wp_links'

class WpOptions(BaseModel):
    autoload = CharField(max_length=20)
    option = BigIntegerField(db_column='option_id', primary_key=True)
    option_name = CharField(max_length=64)
    option_value = TextField()

    class Meta:
        db_table = 'wp_options'

class WpPostmeta(BaseModel):
    meta = BigIntegerField(db_column='meta_id', primary_key=True)
    meta_key = CharField(max_length=255, null=True)
    meta_value = TextField(null=True)
    post = BigIntegerField(db_column='post_id')

    class Meta:
        db_table = 'wp_postmeta'

class WpPosts(BaseModel):
    id = BigIntegerField(db_column='ID', primary_key=True)
    comment_count = BigIntegerField()
    comment_status = CharField(max_length=20)
    guid = CharField(max_length=255)
    menu_order = IntegerField()
    ping_status = CharField(max_length=20)
    pinged = TextField()
    post_author = BigIntegerField()
    post_content = TextField()
    post_content_filtered = TextField()
    post_date = DateTimeField()
    post_date_gmt = DateTimeField()
    post_excerpt = TextField()
    post_mime_type = CharField(max_length=100)
    post_modified = DateTimeField()
    post_modified_gmt = DateTimeField()
    post_name = CharField(max_length=200)
    post_parent = BigIntegerField()
    post_password = CharField(max_length=20)
    post_status = CharField(max_length=20)
    post_title = TextField()
    post_type = CharField(max_length=20)
    to_ping = TextField()

    class Meta:
        db_table = 'wp_posts'

class WpTermRelationships(BaseModel):
    object = BigIntegerField(db_column='object_id', primary_key=True)
    term_order = IntegerField()
    term_taxonomy = BigIntegerField(db_column='term_taxonomy_id')

    class Meta:
        db_table = 'wp_term_relationships'

class WpTermTaxonomy(BaseModel):
    count = BigIntegerField()
    description = TextField()
    parent = BigIntegerField()
    taxonomy = CharField(max_length=32)
    term = BigIntegerField(db_column='term_id')
    term_taxonomy = BigIntegerField(db_column='term_taxonomy_id', primary_key=True)

    class Meta:
        db_table = 'wp_term_taxonomy'

class WpTerms(BaseModel):
    name = CharField(max_length=200)
    slug = CharField(max_length=200)
    term_group = BigIntegerField()
    term = BigIntegerField(db_column='term_id', primary_key=True)

    class Meta:
        db_table = 'wp_terms'

class WpUsermeta(BaseModel):
    meta_key = CharField(max_length=255, null=True)
    meta_value = TextField(null=True)
    umeta = BigIntegerField(db_column='umeta_id', primary_key=True)
    user = BigIntegerField(db_column='user_id')

    class Meta:
        db_table = 'wp_usermeta'

class WpUsers(BaseModel):
    id = BigIntegerField(db_column='ID', primary_key=True)
    display_name = CharField(max_length=250)
    user_activation_key = CharField(max_length=60)
    user_email = CharField(max_length=100)
    user_login = CharField(max_length=60)
    user_nicename = CharField(max_length=50)
    user_pass = CharField(max_length=64)
    user_registered = DateTimeField()
    user_status = IntegerField()
    user_url = CharField(max_length=100)

    class Meta:
        db_table = 'wp_users'

