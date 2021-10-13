odoo.define('survey_theme.styles', function (require) {
    'use strict';


    $(document).ready(function(){
        if(!$(".o_survey_start").length){
            hide_background()
        }else{
            $('button[value="start"').on("click",function(){
                hide_background()
            })
            $(document).on("keydown",function(event){
                if (event.keyCode === 13) {
                    hide_background()
                }
            })
        }

        function show_background(){
            $("#wrapwrap").addClass("background-none")
            $(".o_survey_nav").hide()
        }
        function hide_background(){
            $("#wrapwrap").addClass("background-none")
            $(".o_survey_nav").hide()
            $(".o_survey_form").addClass("without-margin-top")
            $(".o_survey_form_content").addClass("without-margin-top")
        }
    })
});