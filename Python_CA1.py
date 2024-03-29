
import time
import pdb

class StudentRecords:
    def __init__(self, records):
        self.records = records

    #sort them and get the lowest student no and removes it from collection
    def retrieve(self):
        start_time = time.time()
        sorted_records = self.merge_sort(self.records)
        print("--- Merge sort completed in %s seconds ---" % (time.time() - start_time))
      # Student with lowest no is student at first student record. This will show user which is lowest
        print('deleting student with lowest student number: ' + str(sorted_records[0]))
        # pop deletes element of array
        sorted_records.pop(0)
        # This is like saving data or keeping data in sync (Because you have sorted, the first element in array is going to be lowest)Taking sorted records from self records.self recrd isn't aware of the deletion so to sync it properly.
        self.records = sorted_records
        print('Successfully deleted student')
        self.show_menu()

    def add(self):
# initialized the variable. This has validation. It takes student id, student full name, course no etc..we want from user
        student_id = 0
      # created a variable called student_id_loop_active and defined it as true
        student_id_loop_active = True

        student_full_name = ''
        student_full_name_loop_active = True

        student_course_number = ''
        student_course_number_loop_active = True

        while student_id_loop_active:
            student_id = input('Enter your 8 digit student_id > ')
            # gets array of existing_ids
            existing_ids = [i[0] for i in self.records]

            try:
                student_id = int(student_id)
            except:
                print('student_id must be a number with no decimal points')
                               # breaks loop and restarts loop
                continue

            if not len(str(student_id)) == 8:
                print('student_id must be 8 digits long')
                # breaks loop and restarts loop
                continue

            if int(student_id) in existing_ids:
                print('That id already exists')
                # breaks loop and restarts loop
                continue

            print('success! student_id: ' + str(student_id))
            student_id_loop_active = False

        while student_full_name_loop_active:
            student_full_name = input('Enter full name > ')

            if len(student_full_name) == 0:
                print('Please enter a full name')
                continue

            print('student_full_name: ' + str(student_full_name))
            student_full_name_loop_active = False

        while student_course_number_loop_active:
            student_course_number = input('Enter 7 digit course number > ')
            if len(student_course_number) == 0:
                print('Please enter a course number')
                continue

            if not len(str(student_course_number)) == 7:
                print('Course number must be 7 digits long')
                continue

            try:
                student_course_number = int(student_course_number)
            except:
                print('student_course_number must be a number with no decimal points')
                continue

            print('student_course_number: ' + str(student_course_number))

            new_student_array = [student_id, student_full_name, student_course_number]
            self.records.append(new_student_array)
            print('Successfully added: ' + str(new_student_array))
            student_course_number_loop_active = False
        self.show_menu()

    def merge_sort(self, records):
        # Divide section
        # This is base case. This break recursion and prevents infinite stack trace error
        if len(records) == 1:
            return records
        # The records array is recursively broken down until the array only consists of 1 element
        mid = (int(round(len(records) / 2)))
        left_half = self.merge_sort(records[0: mid])
        right_half = self.merge_sort(records[mid: len(records)])

        #conquer section
        sorted_records = []
        offset_left = 0
        offset_right = 0
        # while both left_half and right_half have elements
        while offset_left < len(left_half) and offset_right < len(right_half):
            a = left_half[offset_left]
            b = right_half[offset_right]

            if a <= b:
              sorted_records.append(a)
              offset_left += 1
            else:
              sorted_records.append(b)
              offset_right += 1

        # while left_half has elements
        while offset_left < len(left_half):
            sorted_records.append(left_half[offset_left])
            offset_left += 1

        # while right_half has elements
        while offset_right < len(right_half):
            sorted_records.append(right_half[offset_right])
            offset_right += 1

        return sorted_records

    def show_all_records(self):
            print('** Showing all records **')
            print(self.merge_sort(self.records))
            self.show_menu()
            
    def end_program(self):
        confirm_loop_active = True
        while confirm_loop_active:
            confirm = input('Are you sure you want to exit? This will reset the data. y/n')
            if confirm == 'y':
                print('Bye')
                confirm_loop_active = False
            elif confirm == 'n':
                confirm_loop_active = False
                self.show_menu()
            else: 
                print('Please type either y for yes or n for no')

    def show_menu(self):
        selected_option = 0
        print('*' * 100)
        print('Welcome to Student Records')
        while selected_option != '1' and selected_option != '2'  and selected_option != '3':
            print('Press 1 to execute the retrieve() function')
            print('Press 2 to execute the add() function')
            print('Press 3 to execute the show_all_records() function')
            print('Press 4 to end the program')
            selected_option = input('Enter your option > ')
            print('You have selected: ' + selected_option)
            if selected_option == '1':
                self.retrieve()
            elif selected_option == '2':
                self.add()
            elif selected_option == '3':
                self.show_all_records()
            elif selected_option == '4':
                self.end_program()
            else:
                print('*** Please select either 1,2,3 or 4 ***')

def main():
    s = StudentRecords([
        [7, 'A. John', 'A1234567'],
        [8, 'B. david', 'B1234567'],
        [2, 'C. Live', 'C1234567'],
        [1, 'D. Kevin', 'E1234567'],
        [3, 'E. Steward', 'F1234567'],
        [4, 'F. Garry', 'G1234567'],
        [5, 'G. Mike', 'H1234567'],
        [6, 'H. Loren', 'I1234567'],
        [11111111, 'I. McStudent', 'D1234567']
])
    s.show_menu()

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
