from TerminalNotificationAdapter import TerminalNotificationAdapter  # Note the capitalization
from RestaurantMenu import RestaurantMenu


def main():
    # Create the restaurant menu and set the notification adapter
    restaurant_menu = RestaurantMenu()
    terminal_adapter = TerminalNotificationAdapter()
    restaurant_menu.set_notification_adapter(terminal_adapter)

    # Add new items to the menu
    restaurant_menu.add_item_to_menu("Pizza")
    restaurant_menu.add_item_to_menu("Burger")

if __name__ == "__main__":
    main()
