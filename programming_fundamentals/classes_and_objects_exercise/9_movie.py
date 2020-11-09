class Movie:
	__watched_movies = []
	__total_watched = 0

	def __init__(self, name, director):
		self.name = name
		self.director = director
		self.watched = False

	def change_name(self, name):
		self.name = name

	def change_director(self, director):
		self.director = director

	def watch(self):
		if self.name not in self.__watched_movies:
			self.watched = True
			Movie.__total_watched += 1
			Movie.__watched_movies.append(self.name)

	def __repr__(self):
		return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__total_watched}"
