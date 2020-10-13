# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон.

person_dict = {
    "имя": None
    , "фамилия": None
    , "год рождения": None
    , "город проживания": None
    , "email": None
    , "телефон": None
}
print("Введите ваши данные:")

for k in person_dict:
    person_dict[k] = input(f"{k}:")


def person_view(name="Изя", soname="Шниперсон",
                birth_year="1982", city="Москва",
                email="imizya@go.com", phone="+799983147"):
    person_str = f"{name} {soname}, {birth_year}, {city}, {email}, {phone}"
    return person_str


print(person_view(  name=person_dict["имя"], soname=person_dict["фамилия"],
                    birth_year=person_dict["год рождения"], city=person_dict["город проживания"],
                    email=person_dict["email"], phone=person_dict["телефон"]))
