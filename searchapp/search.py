from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Date, DocType, Text, Field


connections.create_connection()


class PostIndex(DocType):
    """
    Posts model index, DocType is a wrapper so
    your able to write an index like a model and
    retrieve data in the correct format.
    """
    creator = Text()
    publication_date = Date()
    url = Text
    title = Text()
    upvotes = Field(required=False)

    class Meta:
        # Name of the index
        index = "post-index"

