import abc
from users.model import user_model
from users.model import course_model


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, user: user_model.User):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> user_model.User:
        raise NotImplementedError

class AbstractRepositoryC(abc.ABC):   
    @abc.abstractmethod
    def add(self, course: course_model.Course):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> course_model.Course:
        raise NotImplementedError
