# BU Course Catalog API Documentation

## API Call

| Parameter | Value |
| --------- | -------------- |
| Call Type | REST |
| Method    | GET  |

Authentication = api key (can be sent as parameter or header, header is preferred)

URL: https://prod-buprod-fm.snaplogic.io/api/1/rest/feed/run/task/BUProd/Admin-Reporting-And-Analytics/PublicCourseCatalog/getPublicCourseCatalog_triggered
 
Headers:
| Header  | Value |
| ------- | ----- |
| Content-Type | application/json |
| x-api-key | [api key emailed via secure mail. Note that the api key can be sent as a header or parameter but headers are more secure.] |


Parameters:
| Parameter | Value |
| --------- | ----- |
| x-api-key | [api key sent via securemail] |
| term | [specific term to pull courses i.e. ‘2251’ returns Spring 2025, 2255 Summer 2025, 2258 Fall 2025, 2261 Spring 2026, etc.] |
| college | [the college for which to pull classes in the specified term, i.e., CDS, CAS, QST] |


Status Codes:
| Status Code | Status Meaning |
| ----------- | -------------- |
| 200         | Success        |
| 401         | Incorrect Authorization |
| 422         | Input Payload or Parameter data Validation Issue |
| 500         | Snaplogic Service was not successfully reached |
