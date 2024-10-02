def manage_student_database():
    stu_data = []  
    student_id_counter = 1
    
    while True:
        stu_name = input("Please enter the student's name (or type 'stop' to finish): ")
        
        if stu_name.lower() == 'stop':
            break
        else:
            if stu_name in [i[1] for i in stu_data]:
                print("Student already exists in the database. Please enter a different name.")
            else:
                stu_data.append((student_id_counter, stu_name))
                student_id_counter += 1 
    
    
    print("\nComplete List of Students (Tuples):")
    print(stu_data)

    print("\nList of Students with IDs: ")
    for i in  stu_data:
        print(f"ID: {i[0]}, Name: {i[1]}")
        
        
    total_number_of_students = len(stu_data)
    print(f"Total number of students: {total_number_of_students}")
    
    # return stu_data  


students = manage_student_database()
print(students)

