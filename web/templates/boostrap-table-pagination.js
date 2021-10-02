$.fn.pageMe = function(opts){
			var $this = this,
				defaults = {
					perPage: 2,
					showPrevNext: false,
					hidePageNumbers: false,
					targetString: 'all'
				},
				settings = $.extend(defaults, opts);
			
				var listElement = $this;
				var perPage = settings.perPage; 
				var targetString = settings.targetString; 
				var children = listElement.children();
				var filteredElementList = listElement.children();
				var pager = $('.pager');
				pager.empty();
				
				
				if (typeof settings.childSelector!="undefined") {
					children = listElement.find(settings.childSelector);
				}
				
				if (typeof settings.pagerSelector!="undefined") {
					pager = $(settings.pagerSelector);
				}
				
				var index = 0;
				
				if (targetString != 'all') {
					while (index < filteredElementList.size()) {
						
						if (filteredElementList[index].dataset.status != targetString) {							
							filteredElementList.splice(index, 1);
						} else {
							index++;
						}			
					}
				}
					
				
				
				var numItems = 0;
				if (filteredElementList != null) {
					numItems = filteredElementList.length;
				}
				
				var numPages = Math.ceil(numItems/perPage);

				pager.data("curr",0);
				
				if (settings.showPrevNext){
					$('<li><a href="#" class="prev_link">&lt;&lt;</a></li>').appendTo(pager);
				}
				
				var curr = 0;
				while(numPages > 1 && numPages > curr && (settings.hidePageNumbers==false)){
					$('<li><a href="#" class="page_link">'+(curr+1)+'</a></li>').appendTo(pager);
					curr++;
				}
				
				if (settings.showPrevNext){
					$('<li><a href="#" class="next_link">&gt;&gt;</a></li>').appendTo(pager);
				}
				
				pager.find('.page_link:first').addClass('active');
				pager.find('.prev_link').hide();
				if (numPages<=1) {
					pager.find('.next_link').hide();
				}
				pager.children().eq(1).addClass("active");
				
				filteredElementList.hide();
				filteredElementList.slice(0, perPage).show();
				
				pager.find('li .page_link').click(function(){
					var clickedPage = $(this).html().valueOf()-1;
					goTo(clickedPage,perPage);
					return false;
				});
				pager.find('li .prev_link').click(function(){
					previous();
					return false;
				});
				pager.find('li .next_link').click(function(){
					next();
					return false;
				});
				
				function previous(){
					var goToPage = parseInt(pager.data("curr")) - 1;
					goTo(goToPage);
				}
				 
				function next(){
					goToPage = parseInt(pager.data("curr")) + 1;
					goTo(goToPage);
				}
				
				function goTo(page){
					var startAt = page * perPage,
						endOn = startAt + perPage;
					
					filteredElementList.css('display','none').slice(startAt, endOn).show();
					
					if (page>=1) {
						pager.find('.prev_link').show();
					}
					else {
						pager.find('.prev_link').hide();
					}
					
					if (page<(numPages-1)) {
						pager.find('.next_link').show();
					}
					else {
						pager.find('.next_link').hide();
					}
					
					pager.data("curr",page);
					pager.children().removeClass("active");
					pager.children().eq(page+1).addClass("active");
				
				}
			};
			
		$(document).ready(function () {

			$('#myTable').pageMe({pagerSelector:'#myPager',showPrevNext:true,hidePageNumbers:false,perPage:2, targetString:'all'});				

			$('.btn-filter').on('click', function () {
				var $target = $(this).data('target');
				if ($target != 'all') {
					$('.table tr').css('display', 'none');
					$('.table tr[data-status="' + $target + '"]').fadeIn(1);
				} else {
					$('.table tr').css('display', 'none').fadeIn(1);
				}
				$('#myTable').pageMe({pagerSelector:'#myPager',showPrevNext:true,hidePageNumbers:false,perPage:2, targetString:$target});				
			});
		});
