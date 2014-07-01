'use strict';

var ttControllers = angular.module('ttControllers',['LocalStorageModule']);

ttControllers.controller('RegisterCtrl',['$scope', '$http', 
    function($scope, $http){
        $scope.user = {}
        
        $scope.submitForm=function(form){
            $http(
                {
                    method: "POST",
                    url :'http://localhost:5000/api/register',
                    data:JSON.stringify($scope.user),
                    headers: {'Content-Type': 'application/json'}
                }
            ).
            success(function(data, status, headers, config){
                if (data.status === "unsuccess"){
                    $scope.usernameErrorMsg = data.reason;
                }
            });

        }
    }]);

ttControllers.controller('MainpageCtrl', ['$scope', 
    function($scope){
        
    }
])

ttControllers.controller('SignInCtrl', ['$scope', '$http', '$window',  
        function($scope, $http, $window){
            $scope.user = {};
            $scope.submitForm = function(form){
                $http(
                    {
                        method: "POST",
                        url: '/api/signin',
                        data: JSON.stringify($scope.user),
                        headers: {'Content-Type': 'application/json'}
                    }
                ).
                success(function(data, status, headers, config){
                    if (data.status === "unsuccess"){
                        console.log('error');
                        return;
                    }
                    $http.defaults.headers.common['Authentication'] = 'Base ' + data.token;
                    $window.location = '/user_dashboard';
                });
            }
        }]);

ttControllers.controller('DashboardCtrl', ['$scope', function($scope){

}]);


ttControllers.controller('TimeMgmtCtrl', ['$scope', 'localStorageService',
        function($scope, localStorageService){
            
            var taskToTrack = {
                'start_time':0,
                'end_time':0,
                'date':''
            }
            
            $scope.isActive = false;
            
            $scope.startTimeTracking = function(){
                console.log('im going to start time tracking');
                var time = new Date().getTime() / 1000;
                taskToTrack.start_time = time;
                return false;
            }
        }
    ])
