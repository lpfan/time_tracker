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
            $scope.usefull_time = 0;
            $scope.useless_time = 0;
            $scope.total_usefull_time = 0;
            var tickInterval = 1000;

            $scope.usefull_tick = function(){
                $scope.usefull_time += 1;
                $scope.usefull_timer = $timeout($scope.usefull_tick, tickInterval);
            }

            $scope.useless_tick = function(){
                $scope.useless_time += 1;
                $scope.useless_timer = $timeout($scope.useless_tick, tickInterval);
            }

            $scope.format_time = function(raw_seconds){
                var sec_num = parseInt(raw_seconds, 10);
                if (sec_num > 0){
                    var hours = Math.floor(sec_num / 3600);
                    var minutes = Math.floor((sec_num - (hours * 3600))/60);
                    var seconds = sec_num - (hours * 3600) - (minutes * 60);
                    var time = hours + ':' + minutes + ':' + seconds;
                    return time;
                }
                return "0";
            }

            $scope.init = function(){
                //console.log('init');
                var c_date = new Date();
                var s_date = new Date().setHours(10,0,0);
                var seconds = (c_date - s_date)/1000;
                $scope.stopIsDisabled = true;
                var today_str = c_date.getFullYear()+'-'+ parseInt(c_date.getMonth()+1)+'-'+c_date.getDate();
                $http({
                    method: 'POST',
                    url: '/api/sync/init',
                    data: JSON.stringify({'today': today_str})
                }).
                success(function(data, status, headers, config){
                    $scope.total_usefull_time = data['usefull_time'];
                });

                if (seconds > 0){
                    $scope.useless_time = seconds;
                    var timer = $timeout($scope.useless_tick, tickInterval);
                } else {
                    $scope.useless_time = "У вас усе ще попереду";
                }
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
                    $timeout.cancel($scope.useless_timer);
                    $scope.stopIsDisabled = false;
                    $scope.task.uuid = data['uuid']
                    var timer = $timeout($scope.usefull_tick, tickInterval);
                });
                return false;
            }

            $scope.stopTimeTracking = function(){
                var time = new Date();
                $scope.task.end_time = time.getTime() / 1000;
                $scope.task.duration = $scope.usefull_time;
                $timeout.cancel($scope.usefull_timer);
                $scope.total_usefull_time += $scope.usefull_time;
                $scope.usefull_time = 0;
                var timer = $timeout($scope.useless_tick, tickInterval);
                $http({
                    method: 'POST',
                    url: '/api/sync/finish_task',
                    data: JSON.stringify($scope.task),
                    headers: {'Content-Type': 'application/json'}
                }).
                success(function(data, status, headers, config){
                    $scope.stopIsDisabled = true;
                    $scope.isDisabled = false;
                    $scope.newTaskForm.$setPristine();
                    $scope.task = {};
                });
                return false;
            }
        }
    ])
