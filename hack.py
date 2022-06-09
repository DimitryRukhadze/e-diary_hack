import random
import logging

from itertools import zip_longest


import django.core.exceptions

from datacenter.models import Lesson, Schoolkid, Commendation, Chastisement, Mark, Subject


def create_commendation(schoolkid, subject_name):

    subject_lessons = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter,
        subject__title=subject_name
    ).order_by('-date')

    child_commends = Commendation.objects.filter(
        subject__title=subject_name,
        schoolkid=schoolkid
    ).order_by('-created')

    availible_commends = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
    ]

    for lesson, commendation in zip_longest(subject_lessons, child_commends):
        if lesson and not commendation:
            Commendation.objects.create(
                text=random.choice(availible_commends),
                created=lesson.date,
                teacher=lesson.teacher,
                schoolkid=schoolkid,
                subject=lesson.subject
            )
            break


def fix_marks(schoolkid):
    child_marks = Mark.objects.filter(schoolkid=schoolkid.id, points__lt=4)
    for mark in child_marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    child_chasts = Chastisement.objects.filter(schoolkid=schoolkid)
    child_chasts.delete()


def get_similar_names(name_to_search):

    same_name_kids = '\n'.join(
        [
            f'{kid.full_name} {kid.year_of_study}{kid.group_letter}'
            for kid in Schoolkid.objects.filter(
                full_name__contains=name_to_search
                )
        ]
    )

    return same_name_kids


def get_subject_names_for_kid(kid):
    subject_names = '\n'.join(
        [
            subject.title
            for subject in Subject.objects.filter(
                year_of_study=kid.year_of_study
                )
        ]
    )
    return subject_names


def main():
    logging.basicConfig(format=f'%(levelname)s %(message)s')

    kid_name = input('Введите имя ученика: ')
    similar_names = get_similar_names(kid_name)

    try:
        kid_object = Schoolkid.objects.get(full_name__contains=kid_name)
    except django.core.exceptions.MultipleObjectsReturned:
        logging.critical('Много похожих имён. Ввведите одно из них')
        print(similar_names)
        exit()
    except django.core.exceptions.ObjectDoesNotExist:
        logging.critical('Ученика с таким именем нет. Проверьте правильность написания')
        exit()

    kid_subject_names = get_subject_names_for_kid(kid_object)

    try:
        subject_name = input('Введите название предмета: ')
        subject_object = Subject.objects.get(
            title=subject_name,
            year_of_study=kid_object.year_of_study
        )
    except django.core.exceptions.ObjectDoesNotExist:
        logging.critical('Такого урока нет у этого ученика')
        print('Вот правильные названия уроков:')
        print(kid_subject_names)
        exit()

    fix_marks(kid_object)
    remove_chastisements(kid_object)
    create_commendation(kid_object, subject_name)
    print(f'Записи для {kid_name} исправлены. Похвала по {subject_name} добавлена')


if __name__ == '__main__':
    main()