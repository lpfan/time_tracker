'use strict';

var ttApp = angular.module('ttApp', [
    'ngRoute',
    'ttControllers'
]);

ttApp.config(['$routeProvider',
        function($routeProvider){
            $routeProvider.
                when('/register', {
                    templateUrl: '../static/js/register.html',
                    controller: 'RegisterCtrl'
                })
        }]);
