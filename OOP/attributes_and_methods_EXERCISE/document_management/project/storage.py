# from OOP.attributes_and_methods_EXERCISE.document_management.project.category import Category
# from OOP.attributes_and_methods_EXERCISE.document_management.project.document import Document
# from OOP.attributes_and_methods_EXERCISE.document_management.project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        return f'\n'.join(map(str, self.documents))

    @staticmethod
    def find_obj_by_id(id, collection):
        return list(filter(lambda x: x.id == id, collection))[0]

    @staticmethod
    def add(obj, collection):
        if obj not in collection:
            collection.append(obj)

    def edit(self, id, value, attr, collection):
        fount_obj = self.find_obj_by_id(id, collection)
        setattr(fount_obj, attr, value)

    def delete(self, id, collection):
        found_obj = self.find_obj_by_id(id, collection)
        collection.remove(found_obj)

    def add_category(self, category):
        self.add(category, self.categories)

    def add_topic(self, topic):
        self.add(topic, self.topics)

    def add_document(self, document):
        self.add(document, self.documents)

    def edit_category(self, category_id: int, new_name: str):
        self.edit(category_id, new_name, 'name', self.categories)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        self.edit(topic_id, new_topic, 'topic', self.topics)
        self.edit(topic_id, new_storage_folder, 'storage_folder', self.topics)

    def edit_document(self, document_id: int, new_file_name: str):
        self.edit(document_id, new_file_name, 'file_name', self.documents)

    def delete_category(self, category_id):
        self.delete(category_id, self.categories)

    def delete_topic(self, topic_id):
        self.delete(topic_id, self.topics)

    def delete_document(self, document_id):
        self.delete(document_id, self.documents)

    def get_document(self, document_id):
        return self.find_obj_by_id(document_id, self.documents)
