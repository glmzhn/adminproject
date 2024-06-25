1)Админ панель.Интуитивно понятна и соответствует документации.

2)API эндпоинты и как к ним обращаться:
  Всего два эндпоинта, а именно - 'api/v1/categories' - список всех категорий товаров.
  А так же 'api/v1/items' - список всех товаров.
  
  ПРИМЕЧАНИЕ:В поле item_image лежит ссылка на изображение.Так же применимо к следующему эндпоинту.
  
  Как должен выглядеть запрос и ответ:

  HTTP Request
  GET api/v1/items
  
  JSON-responce:
  
      {
            "id": 1,
            "name": "Плитка керамическая",
            "item_image1": "http://localhost:8000/media/item/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-04-20_030510.png",
            "item_image2": "http://localhost:8000/media/item/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-04-17_104357.png",
            "item_image3": "http://localhost:8000/media/item/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-04-03_191750.png",
            "colour": "Бежевый",
            "material": "Керамика",
            "size": "5",
            "thickness": "1.5",
            "place_of_application": "Ванная комната",
            "category": 2
        },
        {
            "id": 2,
            "name": "Шторы тканевые",
            "item_image1": "http://localhost:8000/media/item/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-03-31_023321.png",
            "item_image2": "http://localhost:8000/media/item/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-04-23_155111.png",
            "item_image3": "http://localhost:8000/media/item/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-05-23_163326.png",
            "colour": "Темно-серый",
            "material": "Ткань",
            "size": "6",
            "thickness": "2",
            "place_of_application": "Гостинная",
            "category": 3
        }

  Как должен выглядеть запрос и ответ:

  HTTP Request
  GET api/v1/categories
  
  JSON-responce:
  
      {
            "id": 2,
            "cat_name": "Плитки",
            "cat_image": "http://localhost:8000/media/item%20category/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-04-03_191750.png"
        },
        {
            "id": 3,
            "cat_name": "Шторы",
            "cat_image": "http://localhost:8000/media/item%20category/images/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2024-05-12_155629.png"
        }
