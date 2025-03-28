### Project Structure


src/
└── main/
    ├── java/
    │   └── com.aaron.backend/
    │       ├── config/
    │       │   ├── SecurityConfig.java      # Spring Security configurations
    │       │   └── CorsConfig.java          # CORS setup for front-end communication
    │       ├── controller/
    │       │   ├── AuthController.java      # Handles login, registration, token refresh
    │       │   ├── UserController.java      # For user-specific requests
    │       │   ├── TransactionController.java
    │       │   └── ReceiptController.java
    │       ├── dto/
    │       │   ├── AuthRequest.java         # Login request structure
    │       │   ├── AuthResponse.java        # JWT token response
    │       │   ├── UserRegistrationRequest.java
    │       │   └── ReceiptUploadRequest.java
    │       ├── exception/
    │       │   ├── CustomExceptionHandler.java # Handles global exceptions
    │       │   └── ResourceNotFoundException.java
    │       ├── model/
    │       │   ├── User.java
    │       │   ├── Role.java
    │       │   ├── Receipt.java
    │       │   └── Transaction.java
    │       ├── repository/
    │       │   ├── UserRepository.java
    │       │   ├── RoleRepository.java
    │       │   ├── ReceiptRepository.java
    │       │   └── TransactionRepository.java
    │       ├── security/
    │       │   ├── JwtTokenProvider.java
    │       │   ├── JwtAuthenticationFilter.java
    │       │   └── SecurityConstants.java
    │       ├── service/
    │       │   ├── AuthService.java         # Handles authentication
    │       │   ├── UserService.java         # Handles user operations
    │       │   ├── TransactionService.java  # Fetches transactions
    │       │   └── ReceiptService.java      # Processes receipt uploads
    │       └── FinanceAppApplication.java   # Main application
    └── resources/
        ├── application.yml                  # Configuration with profiles
        ├── data.sql                         # Optional testing data
        └── schema.sql                       # Database schema
