# VibeConnect

VibeConnect is a full-stack social media platform designed to connect users through posts, messaging, and search functionalities. It leverages Vue.js for the frontend and Django for the backend, offering a robust and scalable solution for social networking applications.

## Features

### Posts

- Users can create, edit, and delete posts.
- Posts can include images, videos, or text content.
- Posts are displayed in a chronological order, with options for likes, comments, and shares.

### Messaging

- Real-time messaging system allowing users to send direct messages to each other.
- Support for multimedia messages (text, images, files).
- Notifications for new messages and message status indicators.

### Search

- Powerful search functionality to discover users, posts, and hashtags.
- Filters for refining search results based on various criteria.
- Autocomplete and suggestions for enhancing user experience.

### Authentication and Authorization

- Secure user authentication using Django's built-in authentication system.
- Role-based access control for different user roles (admin, regular user).

### User Profiles

- Customizable user profiles with profile pictures, bio, and social links.
- Followers/following system to connect users within the platform.

### Responsive Design

- Responsive and mobile-friendly design using Vue.js and Bootstrap.
- Ensures a seamless user experience across devices of all sizes.

## Why Vue.js and Django Combination?

### Vue.js (Frontend)

Vue.js was chosen for the frontend of VibeConnect due to its:

- **Reactivity**: Vue's reactive data binding makes it easy to handle dynamic content and state changes in real-time, crucial for a social media platform's interactive features.
- **Component-Based Architecture**: Vue's component-based structure promotes modularity, making it easier to manage complex UI components and reuse code across the application.
- **Performance**: Vue's virtual DOM and efficient rendering ensure fast updates and smooth user interactions, essential for handling large amounts of content and user interactions typical in social media platforms.

### Django (Backend)

Django serves as the backend framework for VibeConnect because of its:

- **Robustness and Scalability**: Django's ORM (Object-Relational Mapping) and built-in features (authentication, admin interface, etc.) provide a solid foundation for developing scalable web applications with minimal boilerplate code.
- **Security**: Django's security features (CSRF protection, SQL injection prevention, etc.) help protect user data and ensure compliance with web security best practices.
- **Ecosystem**: Django's vast ecosystem of packages and libraries (Django REST framework, Django Channels for WebSocket support, etc.) extends its capabilities to handle complex backend requirements efficiently.

## Getting Started

To run VibeConnect locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vibeconnect.git
   cd vibeconnect
   ```

2. Set up the backend (Django):
   ```bash
   cd backend
   # Create and activate virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   # Install dependencies
   pip install -r requirements.txt
   # Run migrations
   python manage.py migrate
   # Start Django development server
   python manage.py runserver
   ```

3. Set up the frontend (Vue.js):
   ```bash
   cd frontend
   # Install dependencies
   npm install
   # Start Vue development server
   npm run serve
   ```

4. Access VibeConnect at `http://localhost:8080` in your web browser.

## Contributing

Contributions to VibeConnect are welcome! If you have suggestions for new features, improvements, or bug fixes, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
