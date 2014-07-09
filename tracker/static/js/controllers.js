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

ttControllers.controller('TimeMgmtCtrl', ['$scope', '$http', '$timeout', 'localStorageService',
        function($scope, $http, $timeout, localStorageService){
            
            var taskToTrack = {
                'start_time':0,
                'end_time':0,
                'date':''
            }

            
            $scope.isDisabled = false;
            $scope.task = {};
            $scope.useful_timer = 0;
            $scope.useless_time = 0;
            $scope.tickInterval = 1000;

            var tick = function(){
                $scope.useful_timer += 1;
                $timeout(tick, $scope.tickInterval);
            }


            $scope.startTimeTracking = function(form){
                var start_time = new Date().getTime()/1000;
                $scope.isDisabled = true;
                $scope.task.start_time = start_time;
                $http({
                    method: 'POST',
                    url: '/api/sync/start_task',
                    data: JSON.stringify($scope.task),
                    headers: {'Content-Type': 'application/json'}
                }).
                success(function(data, status, headers, config){
                    console.log(data);
                    $timeout(tick, $scope.tickInterval);
                });
                return false;
            }

            $scope.stopTimeTracking = function(){
                var time = new Date();
                $scope.task.end_time = time.getTime() / 1000;
                console.log('And then sync it with mongoDb');
                console.log('Total duration is ', $scope.task.end_time - $scope.task.start_time);
                return false;
            }
        }
    ])
