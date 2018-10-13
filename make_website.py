def read_file():
    """
    This function would read the contents of the file in a stream and puts it in a list.
    :return: A list of the content of file
    """
    fstream = open("resume.txt", "r")
    # list of lines from the input file
    lines_list = fstream.readlines()
    fstream.close()
    return lines_list


def detect_name(name):
    """
    This function would detect the name of the person from resume.
    :return: The name of the person if it is error free
    """
    # Ensuring the first character of the name is uppercase
    if not name[0].isupper():
        # raise exception and terminate if not
        print(type(Exception))
        raise Exception("The first line has to be a name with proper capitalization.")
    else:
        return name.strip()


def get_index(string_to_look, file_list):
    """
    This function returns an index of the string given to it as an input from file_list
    :param string_to_look: The string for detection
    :param file_list: list of data read from the file
    :return: The index of the particular string taken as input in the file_list
    """
    # save the index of the string in the file_list
    for index in range(0, len(file_list)):
        if string_to_look in file_list[index]:
            return index
    return -1


def check_email_validity(email):
    """
    This function checks if the email-id is valid.
    :param email: email id of person
    :return: Flag stating if there is an error in the email or not
    """
    set_error_flag = False

    # checking if the first letter after '@' is lowercase
    for i in range(0, len(email)):
        if email[i] == '@':
            break
        # checking if all the characters before @ are alphabets
        if not email[i].isalpha():
            set_error_flag = True
            return set_error_flag

    # check if the letter after @ is lower character
    if not email[i + 1].islower():
        set_error_flag = True

    # checking if the last 4 characters are .com or .edu
    email_length = len(email)
    start_check = email_length - 4
    if '.com' not in email[start_check:email_length]:
        if '.edu' not in email[start_check:email_length]:
            set_error_flag = True

    # check if there are digits/numbers in the email
    if any(ch.isdigit() for ch in email):
        set_error_flag = True

    return set_error_flag


def detect_email(email):
    """
    This function detects the e-mail address and also checks for it's samity.
    :return: E-mail address of the person if it's valid, empty string otherwise.
    """
    # check for email sanity
    set_error_flag = check_email_validity(email)

    # return empty string if there is an error
    if set_error_flag:
        return ""
    # return actual email if valid
    return email.strip()


def detect_courses(courses_string):
    """
    This function detects the courses listed in the resume.
    :return: list of the courses the person has taken
    """
    courses = courses_string.split(",")
    first_course = courses[0]

    for i in range(8, len(first_course)):
        if first_course[i].isalpha():
            break
        courses[0] = first_course[i:len(first_course)].strip()
    return courses


def detect_projects(file_list):
    """
    This function detects the projects in the resume
    :param: A list with file lines
    :return: A list of valid projects
    """
    projects_list = []

    projects_index = get_index("Projects", file_list)
    projects_end_index = get_index("-"*10, file_list)

    # If projects or the project end marker not present, return empty list
    if projects_end_index == -1 or projects_index == -1:
        return projects_list

    # ignore empty lines
    for i in file_list[projects_index+1:projects_end_index]:
        if i.strip():
            # remove the unnecessary whitespaces by stripping
            projects_list += [i.strip()]
    return projects_list


def init_html_file():
    """
    This function sets up the current HTML file for further formatting
    :return: None
    """
    # open and read the lines from file
    f = open("resume.html", "r+")
    lines = f.readlines()

    # clear the file
    f.seek(0)
    f.truncate()

    # delete the unrequired files
    del lines[-1]
    del lines[-1]

    # write the necessary lines to the file and close to save
    f.writelines(lines)
    f.close()


def surround_block(tag, text):
    """
    This function surrounds the given text with the given HTML tag and returns the string
    :param tag: Tag for HTML
    :param text: text for HTML
    :return: The string with HTML atg
    """

    # augment the string to make a proper HTML tag, remove unnecessary spaces
    return '<' + tag.strip() + '>' + text.strip() + '</' + tag.strip() + '>'


def open_file():
    """
    This function opens the HTML file
    :return: the opened HTML file
    """
    f = open("resume.html", "a+")
    return f


def populate_html_file(f):
    """
    This function populates the HTML file that
    :param f: The HTML file that needs to be populated
    :return: None
    """
    line1 = "<div id=\"page-wrap\">"
    f.write("\t")
    f.write(line1)


def populate_basic_info(f, name, email):
    """
    This function populates the HTML file with the name and email
    :param f: the HTML file
    :param name: name string in the file_list
    :param email: email string in the file_list
    :return: None
    """
    # ensure indenting and write the name and email to the HTML file
    f.write("\n\t\t")
    f.write("<div>")
    f.write("\n\t\t")
    f.write(surround_block("h1", detect_name(name)))
    f.write("\n\t\t")
    f.write(surround_block("p", detect_email(email)))
    f.write("\n\t\t")
    f.write("</div>")


def populate_projects(f, file_list):
    """
    This function populates the HTML file with the projects extracted
    :param f: The HTML file you want to write to
    :param file_list: The list of lines from the file
    :return: None
    """
    # ensure indenting and write the projects to the HTML file
    f.write("\n\n\t\t")
    f.write("<div>")
    f.write("\n\t\t")
    f.write(surround_block("h2", "Projects"))
    f.write("\n\t\t")
    f.write("<ul>")
    for i in detect_projects(file_list):
        f.write("\n\t\t")
        f.write(surround_block("li", i.strip()))
    f.write("\n\t\t")
    f.write("</ul>")
    f.write("\n\t\t")
    f.write("</div>")


def populate_courses(f, courses_string):
    """
    This function populates the HTML file with courses and indentation
    :param f: The HTML file to write the courses to
    :param courses_string: The String of courses from the text file
    :return: None
    """
    # ensure indenting and write the projects to the HTML file
    f.write("\n\n\t\t")
    f.write("<div>")
    f.write("\n\t\t")
    f.write(surround_block("h3", "Courses"))
    f.write("\n\t\t")
    f.write(surround_block("span", ','.join(detect_courses(courses_string))))
    f.write("\n\t\t")
    f.write("</div>")


def end_file(f):
    """
    This function populates the HTML file with the HTML end tags required
    :param f: HTML file to write to
    :return: None
    """
    f.write("\n\t")
    f.write("</div>")
    f.write("\n")
    f.write("</body>")
    f.write("\n")
    f.write("</html>")


def close_file(f):
    """
    This function closes the HTML file to save all the changes made
    :param f: the HTML file (edited) that needs to be closed
    :return: None
    """
    f.close()


def main():
    # list of lines from the file
    file_list = read_file()

    # email
    email_index = get_index('@', file_list)
    # if there is no email in the file
    if email_index == -1:
        email = ''
    # if email is present
    else:
        email = file_list[email_index].strip()

    # courses string
    courses_index = get_index('Courses', file_list)
    # if there are no courses in the file
    if courses_index == -1:
        courses_string = ''
    # if courses are present
    else:
        courses_string = file_list[courses_index].strip()

    # Initialization to edit the current html file
    init_html_file()

    # Open the file saved after initialization
    f = open_file()

    # Populate the required page wrap for the division
    populate_html_file(f)

    # Populate name and email in the HTML file
    populate_basic_info(f, file_list[0], email)

    # Populate the HTML file with Projects
    populate_projects(f, file_list)

    # Populate the HTML file with Courses
    populate_courses(f, courses_string)

    # Populate the HTML file with the HTML end tags required
    end_file(f)

    # Close the HTML file to save the data written to file
    close_file(f)


if __name__ == '__main__':
    main()
