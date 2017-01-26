/**
 * @author : abhishek goswami ( Hiro )
 * abhishek goswami
 *
 */

(function($, $d, $w, d, w) {

    var Globals = {
        url : 'http://localhost:8000/api/default'
    }

    $Objects = {}

    _Functions = {

        /**
         * Function that runs on the startup
         */
        init : function() {
            _Functions.ShowLoader();
            _Functions.FetchTweets();
        },

        /**
         * Hides the loader
         */
        HideLoader : function() {
            $Objects.loaderSection.hide();
        },

        /**
         * Shows the loader
         */
        ShowLoader : function() {
            $Objects.loaderSection.show();
        },

        /**
         * Fetches the Tweets by making an ajax call
         */
        FetchTweets : function() {
            $.ajax({
                url : Globals.url,
                type : 'GET',
                dataType : 'json',
                success : function(data) {
                    _Functions.HideLoader();
                    _Functions.PopulateTweetsInDOM(data);
                },
                error : function(error) {
                    console.log(error);
                }
            })
        },

        PopulateTweetsInDOM : function(tweetData) {
            var tweetData = tweetData.fetched_tweets || null;
            if(tweetData) {
                tweetData.forEach(function(data) {
                    $Objects.tweetSection.append('<li>' + data.text + '</li>');
                });
            }
            else {
                alert('No tweets fetched');
            }
        }
    }

    $d.ready(function() {
        $Objects.loaderSection = $('.loaderSection');
        $Objects.tweetSection = $('.tweetSection ul');
        _Functions.init();
    });

})(jQuery, jQuery(document), jQuery(window), document, window);