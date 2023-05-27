
Feature: Check items in cart


  Scenario: User can see items in cart
    Given Get amazon main page
    When Click on Best Sellers tab
    And Click on best selling item
    And Store item name
    And Add item to cart
    And Check cart
    And Store cart item name
    Then Verify correct item is in cart