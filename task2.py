def user_info(name, surname, birthday, city, email, phone):
    return print(name, surname, birthday, city, email, phone)


"""По сути же ниже одна строка, в строку вылезало за границу из-за объема данных"""

user_info(surname='Kortsev',
          name='Matvey',
          city='Samara',
          birthday='26/05/1998',
          phone='+799912345678',
          email='63matvey@gmail.com'
          )