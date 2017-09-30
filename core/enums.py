from enumfields import Enum


class MemberType(Enum):
    STUDENT = 1
    TEACHER = 2
    BOTH = 4

    class Labels:
        STUDENT = "Student"
        TEACHER = "Teacher"
        BOTH = "Both"


class ClusterType(Enum):
    NONPROFIT = 1
    SCHOOL = 2
    UNIVERSITY = 4
    COMPANY = 8

    class Labels:
        SCHOOL = "School"
        UNIVERSITY = "University"
        COMPANY = "Company"
