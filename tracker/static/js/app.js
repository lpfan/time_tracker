'use strict';

var ttApp = angular.module('ttApp', [
    'ngRoute',
    'ttControllers',
    'ttDirectivies'
]);

ttApp.config(['$routeProvider',
        function($routeProvider){
            $routeProvider.
                when('/register', {
                    templateUrl: '../templates/partials/register.html',
                    controller: 'RegisterCtrl'
                }).
                when('/', {
                    templateUrl: '../templates/partials/main_page.html',
                    controller: 'MainpageCtrl'
                })
        }]);
