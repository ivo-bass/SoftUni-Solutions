# from OOP.attributes_and_methods_EXERCISE.document_management.project.category import Category
# from OOP.attributes_and_methods_EXERCISE.document_management.project.topic import Topic


class Document:
    def __init__(self, id: int, category_id: int, topic_id: int, file_name: str):
        self.id = id
        self.category_id = category_id
        self.topic_id = topic_id
        self.file_name = file_name
        self.tags = []

    def __repr__(self):
        return f"Document {self.id}: {self.file_name}; " \
               f"category {self.category_id}, " \
               f"topic {self.topic_id}, " \
               f"tags: {', '.join(self.tags)}"

    @classmethod
    def from_instances(cls, id: int, category, topic, file_name: str):
        return cls(id=id, category_id=category.id, topic_id=topic.id, file_name=file_name)

    def add_tag(self, tag_content: str):
        if tag_content not in self.tags:
            self.tags.append(tag_content)

    def remove_tag(self, tag_content: str):
        if tag_content in self.tags:
            self.tags.remove(tag_content)

    def edit(self, file_name: str):
        self.file_name = file_name
