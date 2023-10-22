class RestaurantMenu:
    def __init__(self):
        self.menu_items = []
        self.notification_adapter = None

    def set_notification_adapter(self, notification_adapter):
        self.notification_adapter = notification_adapter

    def add_item_to_menu(self, item_name):
        self.menu_items.append(item_name)
        if self.notification_adapter:
            message = f"New food added to the menu: {item_name}"
            self.notification_adapter.send_notification(message)
