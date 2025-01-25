from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    age:  int = None
    salary: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    id_meeting: int = None
    ipn_of_the_participant: int = None
    name_of_the_company: str = None

