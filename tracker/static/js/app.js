'use strict';

var ttApp = angular.module('ttApp', [
    'ngRoute',
    'ttControllers'
]);

ttApp.config(['$routeProvider',
        function($routeProvider){
            $routeProvider.
                when('/register', {
                    templateUrl: '../templates/partials/register.html',
                    controller: 'RegisterCtrl'
                })
        }]);
