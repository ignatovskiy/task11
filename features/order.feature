
Feature: Send Order

  Scenario: Submit Order (DDT)
    Given the home page is open
    When the user click on last vehicle in vehicle table
    And the user click on "Purchase order"
    And the user click on "Send order"
    And the user click on "Contact details"
    And enter to Surname "Ignatovsky"
    And enter to First name "Nikita"
    And enter to Street address "Pushkin street, Kolotushkin house"
    And enter to ZIP code "603000"
    And enter to City "Nizhny Novgorod"
    And enter to Country "Russia"
    And enter to Phone number "88005553535"
    And enter to E-mail address "test@mail.ru"
    And the user click on "Send purchase order"
    Then check order is confirmed