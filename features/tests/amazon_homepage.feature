
Feature: Amazon sign in test


  Scenario: User can see sign in page
    #Given Open amazon main page
    When Click orders
    Then Verify sign in page opens


  Scenario: User can see items in cart
    #Given Open amazon main page
    When Click on cart
    Then Verify amazon cart is empty


  Scenario: User can see 5 links on Best Seller page
    #Given Open amazon main page
    When Click on Best Sellers
    Then Verify there are 5 links


  Scenario: User can see items in cart
    #Given Open amazon main page
    When Click on Best Sellers tab
    And Click on best selling item
    And Store item name
    And Add item to cart
    And Check cart
    And Store cart item name
    Then Verify correct item is in cart

 Scenario: Verify that user can search departments
   Given Open amazon main page
   When Select department
   When Search for radio
   Then Verify that correct department is shown