def main():
    student_grades = {}
    print("Введення оцінок студентів")
    print("Вводьте ім'я та оцінку. Для завершення введіть 'stop' замість імені.")

    while True:
        name = input("\nВведіть ім'я студента: ")

        if name.lower() == 'stop':
            print("...Введення даних завершено.")
            break

        while True:
            grade_input = input(f"Введіть оцінку для студента '{name}' (1-12): ")

            try:
                grade = int(grade_input)

                if 1 <= grade <= 12:
                    student_grades[name] = grade
                    print(f"-> Дані збережено: {name} - {grade}")
                    break
                else:
                    print("! Помилка: Оцінка має бути в діапазоні від 1 до 12.")

            except ValueError:
                print("! Помилка: Будь ласка, введіть оцінку цифрою.")

    if not student_grades:
        print("\nВи не ввели жодних даних. Програму завершено.")
        return

    print("\n" + "=" * 30)
    print("📋 Загальний список студентів та оцінок:")
    print("=" * 30)
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

    total_sum = sum(student_grades.values())
    count = len(student_grades)
    average_grade = total_sum / count

    excellent_students = []
    good_count = 0
    lagging_count = 0
    failed_count = 0

    for name, grade in student_grades.items():
        if 10 <= grade <= 12:
            excellent_students.append(name)
        elif 7 <= grade <= 9:
            good_count += 1
        elif 4 <= grade <= 6:
            lagging_count += 1
        elif 1 <= grade <= 3:
            failed_count += 1

    print("\n" + "=" * 30)
    print("📊 Статистика по групі:")
    print("=" * 30)
    print(f"Середній бал по групі: {average_grade:.2f}")

    print("\n--- Категорії студентів ---")

    print(f"🎓 Відмінники (10-12): {len(excellent_students)}")
    if excellent_students:
        print(f"   Імена: {', '.join(excellent_students)}")

    print(f"👍 Хорошисти (7-9): {good_count}")
    print(f"🤔 Відстаючі (4-6): {lagging_count}")
    print(f"📉 Не здали (1-3): {failed_count}")


if __name__ == "__main__":
    main()