# заранее -- код не работает так как хочу , подскажите в чем проблема, показалось что с изначальным сайтом приложенным к заданию не справлюсь
#таккак там днк выводилась в отдельном листе , но поменяв сайт где ответ выводится на той же стр ничего не изменилось
import requests
def get_random_dna_sequence(length: int) -> str:
    """Получает случайную последовательность ДНК из заданного количества нуклеотидов."""

    if length < 1:
        raise ValueError("Количество нуклеотидов должно быть больше 1")

    url = "https://randomgenerate.io/random-dna-sequence-generator"
    #url = "https://www.bioinformatics.org/sms2/random_dna.html"

    params = {
        "length": length,
    }
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise ValueError("Ошибка при получении случайной последовательности ДНК")



    # Проверяем, что ответ содержит строку "sequence="
    if "sequence" not in response.text:
        raise ValueError("Ответ веб-сайта не содержит строки 'sequence='")

    # Получаем последовательность ДНК из ответа
    sequence = response.text.split("tbody")[1]
    print(sequence)

    # Проверяем, что последовательность ДНК начинается с символа ">"
  #  if sequence[0] != ">":
    #    raise ValueError("Последовательность ДНК должна начинаться с символа '>")

    # Проверяем, что последовательность ДНК содержит только буквы A, C, G и T
    for nuc in sequence:
        if nuc not in "ACGT":
           # raise ValueError("Последовательность ДНК должна содержать только буквы A, C, G и T")
           raise ValueError(sequence)

    # Проверяем, что длина последовательности ДНК больше 10
    if len(sequence) <= 10:
        raise ValueError("Длина последовательности ДНК должна быть больше 10")

    # Удаляем скобки в начале и в конце последовательности ДНК
 #   sequence = sequence[1:-1]

    return sequence

sequence = get_random_dna_sequence(1000)

print(sequence)
