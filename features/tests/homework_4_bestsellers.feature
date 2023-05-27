
Feature: Best sellers link check


  Scenario: User can see 5 links on Best Seller page
    Given Get amazon main page
    When Click on Best Sellers
    Then Verify there are 5 links