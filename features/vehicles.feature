Feature: Vehicle

  Scenario: Create a vehicle from the options
    Given the home page is open
    When the user select menu "Options"
    And the user select option "Vehicles..."
    And the user input name "Lada Vesta" with price: "560000"
    And the user press Button "Create"
    Then record is added in the list car

  Scenario: Change the vehicle from the options
    Given the home page is open
    When the user select menu "Options"
    And the user select option "Vehicles..."
    And select the last vehicle if exist and click "Edit"
    And edit to the name "Lada 2107" and to the price "50000"
    And the user press Button "Ok"
    Then last record is changed with name "Lada 2107" and price "50000"

  Scenario: Delete the vehicle from the options
    Given the home page is open
    When the user select menu "Options"
    And the user select option "Vehicles..."
    And the user press Button "Delete"
    Then the last vehicle is deleted

