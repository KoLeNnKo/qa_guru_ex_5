from pathlib import Path
from selene import browser, have


def test_demoqa():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Mike')
    browser.element('#lastName').type('Schofield')
    browser.element('#userEmail').type('Mike_Schofield1311@test.com')

    browser.element('[for="gender-radio-1"]').click()

    browser.element('#userNumber').type('9876543210')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select option[value="1"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select option[value="2002"]').click()
    browser.element('.react-datepicker__day--020').click()

    browser.element('#subjectsInput').type('English').press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()

    picture_path = str(Path(__file__).parent.parent.joinpath('images', '134501.png').resolve())
    browser.element('#uploadPicture').set_value(picture_path)

    browser.element('#currentAddress').type('Москва, Вешняки 18')

    browser.element('#state').click()
    browser.element('[id^="react-select-3-option-"]').element_by(have.text('NCR')).click()

    browser.element('#city').click()
    browser.element('[id^="react-select-4-option-"]').element_by(have.text('Noida')).click()

    browser.element('#submit').click()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))

    browser.all('.table-responsive td:nth-child(2)').should(have.exact_texts(
        'Mike Schofield',
        'Mike_Schofield1311@test.com',
        'Male',
        '9876543210',
        '20 February,2002',
        'English',
        'Sports',
        'test.jpg',
        'Москва, Вешняки 18',
        'NCR Noida'
    ))