import os

settings = {
    'host': os.environ.get('ACCOUNT_HOST', 'https://webdb.documents.azure.com:443/'),
    'master_key': os.environ.get('ACCOUNT_KEY', 'kMCfTa5SD8nObsNQsK7H7BVi3XCbIGuOYiFsOe8sBMdtlSdmCt2LquIxy97roD0o7gD1Dd6UEjlxACDbWOl4ug=='),
    'database_id': os.environ.get('COSMOS_DATABASE', 'VisitCount'),
    'container_id': os.environ.get('COSMOS_CONTAINER', 'Visits'),
    #'database_id': os.environ.get('COSMOS_DATABASE', 'ToDoList'),
    #'container_id': os.environ.get('COSMOS_CONTAINER', 'Items'),
}