# Created by Ricardo at 8/9/2022
Feature: Google basic search


  Scenario: Search for over the garden wall music
      Given User access "https://google.com"
      When User search for "potatoes and molasses"
      Then User must see "Over the garden wall" results