import { Component, Input, OnDestroy, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { combineLatest, of, Subscription } from 'rxjs';
import { debounceTime, startWith } from 'rxjs/operators';
import { IMovie } from '../../models/movie-models';
import { MoviesHttpService } from '../../services/movies-http.service';

@Component({
  selector: 'app-movies-table-container',
  templateUrl: './movies-table-container.component.html',
  styleUrls: ['./movies-table-container.component.scss']
})
export class MoviesTableContainerComponent implements OnInit, OnDestroy {
  
  movies: IMovie[];
  movies2: IMovie[];
  subscriptions: Subscription = new Subscription();
  moviename: string;
  constructor(private moviesHttpService: MoviesHttpService) { }
  textControl = new FormControl("")
  ngOnInit(): void {
    this.subscriptions.add(
      // TODO: assign filtered value (according to Form Input) to this.movies
      // Change all the code below here. This is just an example. 
      // Data should be taken from MoviesHttpService 

      // #region Example Code
      this.moviesHttpService.getTop100Movies().subscribe((movies) => {
        this.movies = movies;
        this.movies2 = movies;
      })
      // #endregion
    )
  }
  ngAfterViewInit(){
    this.textControl.valueChanges.subscribe((textValue)=>{
      this.movies = this.movies2.filter(res=>{
        return res.name.toLocaleLowerCase().match(textValue.toLocaleLowerCase());
      })
    })

  }
  /*search(){
    this.movies = this.movies.filter(res=>{
      return res.name.toLocaleLowerCase().match(this.moviename.toLocaleLowerCase());
    })
  }*/

  ngOnDestroy() {
    this.subscriptions.unsubscribe();
  }

}
