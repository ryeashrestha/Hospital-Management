from Doctor import Doctor
from Patient import Patient

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
        print('Welcome to Hospital Management System.')
        print("-----Login-----")
        #Get the details of the admin

        username = input('Username: ')
        password = input('Password: ')

        # check if the username and password match the registered ones
        #ToDo1
        if  username == self.__username and password == self.__password:
            print('You are now logged in as admin.\n')
            return True
        else:
            return False
    
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        first_name = input('First name: ')
        surname = input('Surname: ')
        speciality = input('Speciality: ')
        return first_name,surname,speciality   

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
        op = input('Choose Option: ')

        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')
            #ToDo4
            first_name , surname,speciality  = self.get_doctor_details()

            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5

                    break # save time and end the loop

            #ToDo6
            doctors.append(Doctor(first_name,surname,speciality))# add the doctor ...
                                                         # ... to the list of doctors
            print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            for index, doctor in enumerate(doctors):
                print(f'{index+1:3}| {doctor.get_first_name()} {doctor.get_surname()} | {doctor.get_speciality()}')


        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index!=False:                
                        break
                    else:
                        print("Doctor not found")

                        # doctor_index is the ID mines one (-1)
                    
                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = (input('Input: ')) # make the user input lowercase

            #ToDo8
            if op == '1':
                new_first_name = input('Updated First name: ')
                doctors[index].set_first_name(new_first_name)
            elif op == '2':
                new_surname = input('Updated Surname: ')
                doctors[index].set_surname(new_surname)
            elif op == '3':
                new_speciality = input('Updated Speciality:')
                doctors[index].set_speciality(new_speciality)

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            doctor_index = int(input('Enter the ID of the doctor to be deleted: '))-1
            #ToDo9
            if self.find_index(doctor_index , doctors):
                doctors.pop(doctor_index)

            else:
                print('The id entered is incorrect')

        # if the id is not in the list of patients1
        else:
            print('Invalid operation choosen. Check your spelling!')

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms |')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms |')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index].full_name())

                print('The patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharged_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")

        patient_index = int(input('Please enter the patient ID: ')) - 1

        #ToDo12
        
        patients.pop(patient_index)
        discharged_patients.append(patients[patient_index])
        print(f'Patient discharged successfully.')
        
        

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms |')
        #ToDo13
        self.view(discharged_patients)

    def print_doctors_details(self, doctors):
        print("-----Doctors-----")
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
    
    def print_patients_details(self,patients):
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode | Symptoms |')
        self.view(patients)


    def group_patients(self,patients):
        grp_patients = {}

        for patient in patients:
            surname = patient.get_surname()
            if surname in grp_patients:
                 grp_patients[surname].append(patient)
                
            else:
                grp_patients[surname] = [patient]

        return grp_patients
    
    def update_details(self ):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = (input('Input: '))

        if op == '1':
            #ToDo14
            username = input('Enter the new admin name: ')
            self.__username = username
            print("The admin name is updated")

        elif op == '2':
            password = int(input('Enter the new password: '))
            # validate the password
            if password == int(input('Enter the new password again: ')):
                self.__password = password
            
            print("The password is updated")

        elif op == '3':
            #ToDo15
            address = input('Enter the address: ')
            self.__address = address
            print("The address is updated")

        else:
            #ToDo16
            print('Invalid Operation')

