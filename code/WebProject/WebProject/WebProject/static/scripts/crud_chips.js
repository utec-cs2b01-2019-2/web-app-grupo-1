$(function(){
    var url = "http://127.0.0.1:8080/chips";
    var db ="http://127.0.0.1:8080/users"
    $("#grid").dxDataGrid({
        dataSource: DevExpress.data.AspNet.createStore({
            key: "id",
            loadUrl: url,
            insertUrl: url,
            updateUrl: url,
            deleteUrl: url,
            onBeforeSend: function(method, ajaxOptions) {
                ajaxOptions.xhrFields = { withCredentials: true };
            }
        }),
        editing: {
            allowAdding: true,
            allowUpdating: true,
            allowDeleting: true
        },
        remoteOperations: true,
        columns: [{
                dataField: "id",
                dataType: "number",
                allowEditing: false},

                {dataField: "code",
                allowEditing: true},

                {dataField: "code_from_user",
                lookup: {
                        dataSource: DevExpress.data.AspNet.createStore
                        ({
                            key: "id",
                            loadUrl: db,
                            onBeforeSend: function(method, ajaxOptions) {
                                ajaxOptions.xhrFields = { withCredentials: true };
                            }
                        }),
                        valueExpr: "id",
                        displayExpr: "username"
                        }
                 }
                ]
                            }).dxDataGrid("instance");
            });
