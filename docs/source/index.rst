ArtifactsAPI
============

The `ArtifactsAPI` class provides methods to interact with the Artifacts MMO API, manage character data, perform in-game actions, and handle API requests with built-in cooldown management.

Methods
-------

__init__(self, api_key: str, character_name: str) -> None
---------------------------------------------------------

Initializes the `ArtifactsAPI` instance with the provided API key and character name.

**Parameters:**
- `api_key (str)`: The API key used for authentication.
- `character_name (str)`: The name of the character for which data will be fetched.

_make_request(self, method: str, endpoint: str, json: Optional[dict] = None, source: Optional[str] = None, retries: int = 3, include_headers: bool = False) -> dict
------------------------------------------------------------------------------------------------------------------------------------------------------

Makes an API request and returns the JSON response.

**Parameters:**
- `method (str)`: The HTTP method (e.g., GET, POST) for the request.
- `endpoint (str)`: The API endpoint to send the request to.
- `json (Optional[dict])`: JSON data to send with the request (if applicable).
- `source (Optional[str])`: Optional source identifier for logging.
- `retries (int)`: Number of retries if the request fails (default: 3).
- `include_headers (bool)`: If `True`, the response headers will be included in the return value.

**Returns:**
- `dict`: The JSON response from the API request.

_start_task_loop(self, function, timeout)
------------------------------------------

Starts a task loop that runs the given `function` at the specified `timeout` interval.

**Parameters:**
- `function`: The function to be executed in the loop.
- `timeout`: The time in seconds between each execution of the `function`.

_set_task_loop(self, function=None, timeout=None, thread=None)
--------------------------------------------------------------

Sets a task loop for executing a function periodically. It spawns a new thread to handle the loop.

**Parameters:**
- `function`: The function to be executed in the loop.
- `timeout`: The time in seconds between each execution of the function.
- `thread`: The thread object used for execution.

_get_version(self) -> str
-------------------------

Fetches the version information of the Artifacts API.

**Returns:**
- `str`: The version of the API.

_cache(self)
------------

Checks and updates the cache expiration time, and reloads data for maps, items, monsters, resources, tasks, rewards, achievements, etc.

_raise(self, code: int, m: str) -> None
--------------------------------------

Raises an exception based on the provided HTTP response code and error message.

**Parameters:**
- `code (int)`: The HTTP status code returned by the API.
- `m (str)`: The error message.

**Raises:**
- Various exceptions from `APIException` depending on the response code.

get_character(self, data: Optional[dict] = None, character_name: Optional[str] = None) -> PlayerData
---------------------------------------------------------------------------------------------------

Fetches or updates the character's data and initializes the `char` attribute.

**Parameters:**
- `data (Optional[dict])`: Pre-loaded character data; if `None`, data will be fetched from the API.
- `character_name (Optional[str])`: The name of the character; only used if `data` is `None`.

**Returns:**
- `PlayerData`: The `PlayerData` object with the character's information, including inventory and attributes.

Attributes
----------

- `logger`: The logger instance used for logging events.
- `token`: The API key used for authentication.
- `base_url`: The base URL for the API.
- `headers`: The headers used for API requests, including the authorization token.
- `char`: The `PlayerData` object representing the character data.
- `account`: The `Account` subclass instance.
- `character`: The `Character` subclass instance.
- `actions`: The `Actions` subclass instance.
- `maps`: The `Maps` subclass instance.
- `items`: The `Items` subclass instance.
- `monsters`: The `Monsters` subclass instance.
- `resources`: The `Resources` subclass instance.
- `events`: The `Events` subclass instance.
- `ge`: The `GE` subclass instance.
- `tasks`: The `Tasks` subclass instance.
- `task_rewards`: The `Rewards` subclass instance.
- `achievements`: The `Achievements` subclass instance.
- `leaderboard`: The `Leaderboard` subclass instance.
- `accounts`: The `Accounts` subclass instance.
- `content_maps`: The `ContentMaps` subclass instance.

Exceptions
----------

The class raises various exceptions from `APIException` based on the API response code. Examples include:

- `APIException.NotFound`: Raised when a resource is not found (HTTP 404).
- `APIException.InsufficientQuantity`: Raised when there is not enough of an item (HTTP 478).
- `APIException.ActionAlreadyInProgress`: Raised when an action is already in progress (HTTP 486).
- `APIException.TooLowLevel`: Raised when the character level is too low for an action (HTTP 493).
- `APIException.InventoryFull`: Raised when the inventory is full (HTTP 497).
- `APIException.CharacterNotFound`: Raised when the character is not found (HTTP 498).
- `APIException.CharacterInCooldown`: Raised when the character is in cooldown (HTTP 499).

Logging
-------

The class uses Python's built-in `logging` module to log debug, info, and warning messages. Logs are formatted with the following structure:
`[LEVEL] YYYY-MM-DD HH:MM:SS - CharacterName: Message`
  
The `logger` is configured to output logs to the console.
