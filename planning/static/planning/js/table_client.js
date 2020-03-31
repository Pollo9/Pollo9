$(document).ready(function() 
{
    //Create the table
    var table = $('#kt_table').DataTable
    ( 
        {
            "ajax": 
            {
                "url": "/ajax_clients",
                "type": "GET",
                "dataType": "json",
                "async": true,
                "dataSrc": ""
            },
            "order": [[ 4, "asc" ]],
            "language": 
            {
                "url": "//cdn.datatables.net/plug-ins/1.10.20/i18n/French.json"
            },
            "columns": 
            [
                {
                    "render": function ( data, type, row )
                    {
                        var id = row.pk;
                        return (`
                            <label class="kt-checkbox kt-checkbox--single kt-checkbox--solid" for="` + id + `">
                                <input type="checkbox" value="` + id + `" id="` + id + `" name="client_selectionne" class="kt-checkable">
                                <span></span>
                            </label>`);
                    },
                    "orderable": false,
                    "width": "1%",
                },
                {
                    "render": function ( data, type, row )
                    {
                        var nom = row.fields.nom;
                        var avatar = row.fields.avatar;
                        var url_profil = "/profil_client/" + row.pk;
                        return (`
                            <span>
                                <div class="kt-user-card-v2">
                                    <div class="kt-user-card-v2__pic">
                                        <img src="` + avatar + `" alt="photo">
                                    </div>
                                    <div class="kt-user-card-v2__details">
                                        <a href="` + url_profil + `" class="kt-user-card-v2__name">` + nom + `</a>
                                    </div>
                                </div>
                            </span>`);
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var couleur = row .fields.couleur
                        return (`
                            <span class="kt-badge kt-badge--inline kt-badge--pill" style="background: `+ couleur +`; height: 25px; width: 100px; border: 3px solid #f3f2f7;"></span>
                            `);
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var date_joined = row.fields.date_joined;
                        var res = '';
                        if (date_joined != "None")
                        {
                            var options = {year: 'numeric', month: 'long', day: 'numeric',hour: 'numeric', minute:'numeric'};
                            var date_joined = new Date(date_joined)
                            res += date_joined.toLocaleDateString('fr-FR',options);
                        }
                        return res; 
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var id = row.pk;
                        var archive = row.fields.archive;
                        var res = '';
                        if (archive == false)
                        {
                            return (`<span class="kt-badge kt-badge--info kt-badge--inline" id="active_`+id+`">Actif</span>`);
                        }
                        else
                        {
                            return (`<span class="badge badge-secondary" id="active_`+id+`">Archive</span>`);
                        }
                    }
                },
                {
                    "render": function ( data, type, row )
                    {
                        var csrf = "{% csrf_token %}"
                        var id = row.pk;
                        var nom = row.fields.nom;
                        var url_profil = "/profil_client/" + id;
                        var is_active = row.fields.archive;
                        return (`
                            <a id="button" href="` + url_profil + `" class="btn btn-sm btn-clean btn-icon btn-icon-md" style="padding: 0.06rem .25rem;" title="Profil du client">
                                <i class="icon-eye"></i>
                            </a>
                            <a class="btn btn-sm btn-clean btn-icon btn-icon-md" style="padding: 0.06rem .25rem;" onclick="openModalDelete('` + nom + `',` + id + `)" id="supprimer_client_` + id + `" alt="Supprimer" title="Supprimer le client" data-id=` + id + `>
                                <i class="icon-trash"></i>
                            </a>`);
                    }

                }
            ]
        }
    );

    // Check/uncheck all checkboxes in the table
    $('#select_all1').on('click', function()
    {
        var rows = table.rows({ 'search': 'applied' }).nodes();
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
        if (document.getElementById('select_all2').checked == true)
        {
            document.getElementById('select_all2').checked = false;
        }
        else
        {
            document.getElementById('select_all2').checked = true;
        }
    });

    // Check/uncheck all checkboxes in the table
    $('#select_all2').on('click', function()
    {
        var rows = table.rows({ 'search': 'applied' }).nodes();
        $('input[type="checkbox"]', rows).prop('checked', this.checked);
        if (document.getElementById('select_all1').checked == true)
        {
            document.getElementById('select_all1').checked = false;
        }
        else
        {
            document.getElementById('select_all1').checked = true;
        }
    });

    // When a checkboxe is cheked display menu
    $('#kt_table').on('click',"input[type='checkbox']", function()
    {
        var nombre_row_checked = $('input[name="client_selectionne"]:checked').length;
        var total_rows = table.rows().count()
        if (nombre_row_checked > 0)
        {
            document.getElementById("nombre_de_client").innerHTML = nombre_row_checked + " sélectionnées";
            document.getElementById('menu_to_display').style.display = 'flex';
        }
        else
        {
            document.getElementById("nombre_de_client").innerHTML = total_rows + " total";
            document.getElementById('menu_to_display').style.display = 'none';
        }
        var row = $(this).closest('tr');
        if(this.checked)
        {
            row.addClass('selected');
        } 
        else 
        {
            row.removeClass('selected');
        }     
    });
});